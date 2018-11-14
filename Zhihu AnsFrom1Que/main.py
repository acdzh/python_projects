from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException
import time
from aip import AipNlp
import json

t = "&"
ZHIHU_ID = 'xxxxxxxxxxxxxxxx' #邮箱或者手机号（手机号需带+86前缀）
ZHIHU_KEY = 'xxxxxxxxx' #知乎密码
QUESTION_ID = 123456789 #问题编号
APP_ID = 'xxxxxx' #百度api
API_KEY = 'xxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxx'
baidu_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False
def is_alphabet( uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False
def format_str(content):
    #content = unicode(content, 'utf-8')
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str = content_str+i
    return content_str
def format_time(unix_time):
    st = time.localtime(unix_time)
    st = time.strftime('%Y/%m/%d', st)
    return st


def ai_get(content):
    text = content
    result=baidu_client.sentimentClassify(text)

    print(result)
    print('\n')

    confidence = result['items'][0]['confidence']#可信度
    positive_prob = result['items'][0]['positive_prob']#积极度
    negative_prob = result['items'][0]['negative_prob']#消极度
    sentiment = result['items'][0]['sentiment']#情感倾向
    if sentiment == 0:
        str_sentiment = '负向'
    if sentiment == 1:
        str_sentiment = '中性'
    if sentiment == 2:
        str_sentiment = '正向'

    out = {}
    out['confidence'] = str(confidence)
    out['positive'] = str(positive_prob)
    out['negative'] = str(negative_prob)
    out['sentiment'] = str_sentiment

    return out



client = ZhihuClient()
#登录部分
try:
    client.login(ZHIHU_ID, ZHIHU_KEY)
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login(ZHIHU_ID, ZHIHU_KEY, captcha)


the_question = client.question(QUESTION_ID)


print(the_question.title)



a = 0


with open('all_answers.txt', 'w') as f_txt:
    f_txt.write("昵称&用户关注数&用户粉丝数&用户回答数&用户获赞数&用户获得感谢数&用户性别&用户学校&用户学院&回答内容（去标点符号）&回答日期&最后修改日期&赞数&感谢数&评论数&是否允许评论&是否被建议修改&回答可信度指数&情感分析积极性&情感分析消极性&情感倾向&回答内容")
    for the_answer in the_question.answers:

        the_author = the_answer.author
        author_name = the_author.name
        if author_name == "匿名用户":
            author_following = ''
            author_follower = ''
            author_answers = ''
            author_voteups = ''
            author_thanks = ''
            author_sex = ''
            author_school = ''
            author_major = ''
        else:
            author_following = str(the_author.following_count)
            author_follower = str(the_author.follower_count)
            author_answers = str(the_author.answer_count)
            author_voteups = str(the_author.voteup_count)
            author_thanks = str(the_author.thanked_count)
            author_sex = str(the_author.gender)
            for education in the_author.educations:
                if 'school' in education:
                    author_school = education.school.name
                else:
                    author_school = '未填写'
                if 'major' in the_author.educations:
                    author_major = education.major.name
                else:
                    author_major = '未填写'

        content = format_str(the_answer.content)
        if content == "":
            content = "."
        created_time = format_time(int(the_answer.created_time))
        updated_time = format_time(int(the_answer.updated_time))
        voteups = the_answer.voteup_count
        thanks = the_answer.thanks_count
        int_comments = 0
        for comment in the_answer.comments:
            int_comments = int_comments + 1
        comments = str(int_comments)
        can_comment = the_answer.comment_permission
        if_need_edit = str(the_answer.suggest_edit.status) + "（" + the_answer.suggest_edit.reason + "）"



        judge = ai_get(content[0:255])
        confidence = judge['confidence']
        positive = judge['positive']
        negative = judge['negative']
        sentiment = judge['sentiment']


        out_author = author_name +t+ author_following +t+ author_follower +t+ author_answers +t+ author_voteups +t+ author_thanks +t+ author_sex +t+ author_school + t + author_major +t
        out_ans = content +t+ str(created_time) +t+ str(updated_time) +t+ str(voteups) +t+ str(thanks) +t+ str(comments) +t+ str(can_comment) +t+ str(if_need_edit) + confidence +t+ positive +t+negative +t+ sentiment
        out = out_author + out_ans

        a = a + 1
        print(str(a) + "  " + out)
        f_txt.write(out)
        f_txt.write('\n')
