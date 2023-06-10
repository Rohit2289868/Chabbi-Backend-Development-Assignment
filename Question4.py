def f(dic):
    new_dict = {}
    for key, value in dic.items():
        new_dict[value] = key
    return new_dict
        

        
ans = f({
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
})
print(ans)
