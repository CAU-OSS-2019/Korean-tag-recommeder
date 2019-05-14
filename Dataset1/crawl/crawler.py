import json
import os
from collections import deque
from re import findall
from time import time, sleep
from util import randselect, byteify, file_to_list
import csv

def crawl(api, hashtag, config):
	# print('Crawling started at origin hashtag', origin['user']['username'], 'with ID', origin['user']['pk'])
	if visit_profile(api, hashtag, config):
		pass

def visit_profile(api, hashtag, config):
	while True:
		try:

			processed_tagfeed = {
				'posts' : []
			}
			feed = get_posts(api, hashtag, config)
			
			print('post finish1')
			
			#with open(config['profile_path'] + os.sep + str(hashtag) + '_rawfeed.json', 'w', encoding='UTF-8') as outfile:
			#		json.dump(feed, outfile, indent=2, ensure_ascii=False)
			profile_dic = {}
			posts = [beautify_post(api, post, profile_dic) for post in feed]
			
			print('post finish2')
			
			posts = list(filter(lambda x: not x is None, posts))
			if len(posts) < config['min_collect_media']:
				return False
			else:
				processed_tagfeed['posts'] = posts[:config['max_collect_media']]

			try:
				if not os.path.exists(config['profile_path'] + os.sep): os.makedirs(config['profile_path'])  
			except Exception as e:
				print('exception in profile path')
				raise e

			try:
				with open(config['profile_path'] + os.sep + str(hashtag) + '.json', 'w', encoding='UTF-8') as outfile:
					json.dump(processed_tagfeed, outfile, indent=2, ensure_ascii=False)
			except Exception as e:
				print('exception while dumping')
				raise e
		except Exception as e:
			print('exception while visiting profile', e)
			if str(e) == '-':
				raise e
			return False
		else:
			return True

def beautify_post(api, post, profile_dic):
	try:
		if post['media_type'] != 1: # If post is not a single image media
			return None
		keys = post.keys()
		# print(post)
		user_id = post['user']['pk']
		profile = profile_dic.get(user_id, False)
		while True:
			try:
				sleep(0.05)
				if not profile:
					profile = api.user_info(user_id)
					profile_dic[user_id] = profile
					print('불러오기')
			except Exception as e:
			# print(post)
				print('기다리면된다exception in getting user_info from {} {}'.format(user_id, post['user']['username']), e)
				sleep(5)
				continue
				 
			else:
				break
		# profile = api.username_info('simon_oncepiglet')
		# print(profile)
		# print('Visiting:', profile['user']['username'])
		processed_media = {
			'caption' : post['caption']['text'] if 'caption' in keys and post['caption'] is not None else ''
		}
		processed_media['tags'] = findall(r'#[^#\s]*', processed_media['caption'])
		# print(processed_media['tags'])
		print('저장됨')
		return processed_media
	except Exception as e:
		print('exception in beautify post')
		raise e

def get_posts(api, hashtag, config):
	try:
		feed = []
		try:
			uuid = api.generate_uuid(return_hex=False, seed='0')
			results = api.feed_tag(hashtag, rank_token=uuid, min_timestamp=config['min_timestamp'])
		except Exception as e:
			print('exception while getting feed1')
			raise e
		feed.extend(results.get('items', []))

		if config['min_timestamp'] is not None: return feed

		next_max_id = results.get('next_max_id')
		while next_max_id and len(feed) < config['max_collect_media']:
			print("next_max_id", next_max_id, "len(feed) < max_collect_media", len(feed) < config['max_collect_media'] , len(feed))
			try:
				results = api.feed_tag(hashtag, rank_token=uuid, max_id=next_max_id)
			except Exception as e:
				print('exception while getting feed2')
				if str(e) == 'Bad Request: Please wait a few minutes before you try again.':
					sleep(60)
				else:
					raise e
			feed.extend(results.get('items', []))
			next_max_id = results.get('next_max_id')

		return feed

	except Exception as e:
		print('exception while getting posts')
		raise e

