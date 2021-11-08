local matches = redis.call('KEYS', '*')

redis.log(redis.LOG_WARNING, "Script started")
while 1 do
    for _,key in ipairs(matches) do
        local val = redis.call('GET', key)
    end
end
redis.log(redis.LOG_WARNING, "Script finished")
