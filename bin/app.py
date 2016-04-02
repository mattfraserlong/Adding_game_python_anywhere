import web
from random import randint

target = []
sum_answer = 0
rand_one_add = 0
rand_two_add = 0
count = 0
size = 0

urls = (
    '/', 'Index',
    '/dummy', 'Dummy',
    '/addanswer', 'Addanswer'
)
app = web.application(urls, globals())
app = app.wsgifunc()

render = web.template.render('/home/mattfraserlong/Adding_game_new/templates/', globals={
    'randint': randint,
    'target': target,
    'str': str,
    'sum_answer': sum_answer,
    'rand_one_add': rand_one_add,
    'rand_two_add': rand_two_add,
    'count': count,
    'size': size
})

class Index(object):
    def GET(self):
        return render.game_start()

    def POST(self):
        global count
        form = web.input(name="choice")
        if form.choice == "a":
            return render.addition()
        elif form.choice == "s":
            return render.subtraction()
        elif form.choice == "m":
            return render.multiplication()
        elif form.choice == "d":
            return render.division()
        elif form.choice == "Yes":
            count = 0
            return render.game_start()
        else:
            return render.dummy()

class Dummy(object):
    def POST(self):
        global count
        global size
        global target
        form = web.input(name="choice")
        if form.choice == "Yes":
            count += 1
            return render.game_start()
        elif form.choice == "No":
            size -= 1
            return render.game_over2()
        else:
            return render.dummy()

class Addanswer(object):
    def POST(self):
        form = web.input(name="addchoice")
        if form.addchoice == str(target[count]):
            return render.congrats()
        else:
            return render.game_over()

# To do: extend to all operators
# To do: Host on real server



if __name__ == "__main__":

    app.run()
