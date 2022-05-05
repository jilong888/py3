test20_linear_redis_ip="172.18.6.73";
test20_contract_redis_ip="172.18.6.124";test20_contract_kline_redis_ip="172.18.6.125"
redisConf={
"20l":
    {"kline":[test20_linear_redis_ip,[7002],''],None:[test20_linear_redis_ip,[6385,6386],"rNEAz9uFwHoymy5i"],"index":[test20_linear_redis_ip,[9004],'']},
"20c":
    {"kline":[test20_contract_kline_redis_ip,[7000],''],None:[test20_contract_redis_ip,[6379,6383],"rNEAz9uFwHoymy5i"],"index":[test20_linear_redis_ip,[9004],'']},
}

# print(redisConf['20l'][0]['kline'])