'''
練習 25

寫一個函示 myxml(), 此函式根據填入的參數不同, 傳回結果如下 :

呼叫                                 |傳回值
-------------------------------------|-------------------------------------
myxml('foo')                         |<foo></foo>
-------------------------------------|-------------------------------------
myxml('foo', 'bar')                  |<foo>bar</foo>
-------------------------------------|-------------------------------------
myxml('foo', 'bar', a=1, b=2, c=3)   |<foo a="1" b="2" c="3">bar</foo>
-------------------------------------|-------------------------------------

第一個參數(必填)是 XML tag 或 markup,
第二個參數(選填)是 content (夾在 tag 之間的內容),
其餘數量不定的選擇性參數是放在 tag 裡面的屬性, 以指名方式傳值

'''

def myxml(tag, content='', **kwargs): # 因為 content 是選填, 所以如果沒值就自帶一個空字串
                                      # kwargs 是一個 dict, 有 key, value

    result = list()
    for key,value in kwargs.items():
        result.append(f' {key}="{value}"')
    result_string = ''.join(result)

    return f'<{tag}{result_string}>{content}</{tag}>'

print(myxml('foo', 'bar', a=1, b=2, c=3))
print(myxml('foo', 'bar'))
print(myxml('foo'))

