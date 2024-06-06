# import logging
# import time
# from threading import Lock
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# class CacheManager:
#     def __init__(self, expiration_time=3600):
#         """
#         Initialize the CacheManager with an empty cache, a lock for thread safety, and expiration time.
#
#         :param expiration_time: Time in seconds before cache entries expire.
#         """
#         self.cache = {}
#         self.lock = Lock()
#         self.expiration_time = expiration_time
#
#     def _is_expired(self, timestamp):
#         """
#         Check if the cache entry is expired.
#
#         :param timestamp: The timestamp of the cache entry.
#         :return: True if expired, False otherwise.
#         """
#         return time.time() - timestamp > self.expiration_time
#
#     def _cleanup_cache(self):
#         """
#         Remove expired entries from the cache.
#         """
#         current_time = time.time()
#         with self.lock:
#             expired_keys = [key for key, (_, timestamp) in self.cache.items() if current_time - timestamp > self.expiration_time]
#             for key in expired_keys:
#                 del self.cache[key]
#                 logger.info("Removed expired cache entry for key: %s", key)
#
#     def get_from_cache(self, class_name, user_question):
#         """
#         Retrieve a response from the cache if available and not expired.
#
#         :param class_name: The class name associated with the question.
#         :param user_question: The user's question.
#         :return: The cached answer or None if not found or expired.
#         """
#         key = (class_name, user_question)
#         with self.lock:
#             if key in self.cache:
#                 answer, timestamp = self.cache[key]
#                 if not self._is_expired(timestamp):
#                     logger.info("Cache hit for key: %s", key)
#                     return answer
#                 else:
#                     logger.info("Cache expired for key: %s", key)
#                     del self.cache[key]
#             else:
#                 logger.info("Cache miss for key: %s", key)
#             return None
#
#     def add_to_cache(self, class_name, user_question, answer):
#         """
#         Add a response to the cache with the current timestamp.
#
#         :param class_name: The class name associated with the question.
#         :param user_question: The user's question.
#         :param answer: The answer to cache.
#         """
#         key = (class_name, user_question)
#         with self.lock:
#             self.cache[key] = (answer, time.time())
#             logger.info("Added to cache with key: %s", key)
#
#     def cleanup(self):
#         """
#         Public method to trigger cache cleanup.
#         """
#         self._cleanup_cache()
import logging
import redis

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CacheManager:
    def __init__(self, expiration_time=3600, redis_host='localhost', redis_port=6379):
        """
        Initialize the CacheManager with expiration time and a Redis connection.

        :param expiration_time: Time in seconds before cache entries expire.
        :param redis_host: Redis server hostname.
        :param redis_port: Redis server port.
        """
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        self.expiration_time = expiration_time

    def get_from_cache(self, class_name, user_question):
        """
        Retrieve a response from the Redis cache if available and not expired.

        :param class_name: The class name associated with the question.
        :param user_question: The user's question.
        :return: The cached answer or None if not found or expired.
        """
        key = f"{class_name}:{user_question}"
        cached_response = self.redis_client.get(key)
        if cached_response:
            logger.info("Cache hit for key: %s", key)
            return cached_response
        else:
            logger.info("Cache miss for key: %s", key)
            return None

    def add_to_cache(self, class_name, user_question, answer):
        """
        Add a response to the Redis cache with expiration time.

        :param class_name: The class name associated with the question.
        :param user_question: The user's question.
        :param answer: The answer to cache.
        """
        key = f"{class_name}:{user_question}"
        self.redis_client.setex(key, self.expiration_time, answer)
        logger.info("Added to cache with key: %s", key)
