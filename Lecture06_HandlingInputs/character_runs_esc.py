from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True  # heap에 만들어지는 변수
x = 0
frame = 0


def handle_events():
    # running = False // running과 다른 공간에 있는 변수 / stack에 만들어지는 변수
    global running  # 바깥에 정의된 running을 쓰겠다는 표현 : global
    # running = False  // 이 부분은 바깥의 running 변수를 쓰는 것!
    events = get_events()   # 이벤트를 부르는 과정
    for event in events:    # 이벤트 list에 담겨있는 각각의 이벤트를 하나씩 꺼내는 과정
        # 이벤트의 타입을 살펴보는(비교하는) 과정
        if event.type == SDL_QUIT:  # x(종료)버튼을 눌렀을 때 발생
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass


while x < 800 and running:  # x < 800이고 running이 True이면 작동
    # running 은 루프컨트롤 변수
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 1
    delay(0.01)

close_canvas()

