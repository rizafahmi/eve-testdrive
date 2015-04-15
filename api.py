from eve import Eve
import redis
import settings

r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DBNAME)

app = Eve(redis=r)

if __name__ == '__main__':
    app.run(debug=True)
