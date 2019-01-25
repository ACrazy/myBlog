from flask import Flask, render_template, request
import editPost
import sendMessage

app = Flask(__name__)  # 一个Flask类的对象
app.debug = False

@app.route('/', methods=['GET', "POST"])
def index1():
    allPosts = editPost.indexPosts()
    # print(allPosts)
    return render_template('index.html', result=allPosts)

@app.route('/posts', methods=['GET', "POST"])
def index2():
    postID = request.args.get('name')
    post = editPost.selectPosts(postID)
    return render_template('post.html', result=post)

@app.route('/about', methods=['GET', "POST"])
def index3():
    name = ""
    email = ""
    message = ""
    if request.method == 'POST':
        name = request.form.get('Name')  # 获取POST传过来的值
        email = request.form.get('email')  # 获取POST传过来的值
        message = request.form.get('message')  # 获取POST传过来的值
        state = sendMessage.sendMail(str(message), str(email), str(name))
        print(state)
        return render_template('about.html', state=state)
    return render_template('about.html')

@app.route('/search', methods=['GET', "POST"])
def index4():
    content = ""
    if request.method == 'POST':
        content = request.form.get('Search')
        searchResult = editPost.searchPost(str(content))
        # print(searchResult)
        return render_template('searchPost.html', result=searchResult)
    return render_template('search.html')

@app.route('/type', methods=['GET', "POST"])
def index5():
    postType = editPost.postsType()
    return render_template('type.html', result=postType)

@app.route('/edit', methods=['GET', "POST"])
def index6():
    message = ""
    if request.method == 'POST':
        message = request.form.get('content')
        state = editPost.submitPosts(str(message))
        print(state)
        return render_template('edit.html', state=state)
    return render_template('edit.html')

@app.route('/typeDetial', methods=['GET', "POST"])
def index7():
    types = request.args.get('name')
    post = editPost.selectPoststype(types)
    return render_template('typeDetail.html', result=post)

@app.route('/olderPost', methods=['GET', "POST"])
def index8():
    postType = editPost.postsType()
    return render_template('olderPost.html', result=postType)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
