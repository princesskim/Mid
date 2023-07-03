# VMP_mid

Introduction to Visual Media Programming midterm project

업로드한 항목은 아래와 같습니다.

(1) 사진(.png)과 폰트(.ttf) 파일이 들어있는 assets 파일

(2) 사운드(.mp3) 파일이 들어있는 piano 파일

(3) 4개의 source codes


Mid_clock.py

Tutorial
상,하 방향키는 1분의 시간을 좌, 우 방향키는 5분의 시간을 변경할 수 있다.
초침 소리로 똑딱 소리가 나며, 정각에는 벨소리가 울린다.


Mid_robot3arm.py

Tutorial
q, w는 첫 번째 arm의 각도를 조절한다. 
a, s는 두 번째 arm의 각도를 조절한다. 
z, x는 세 번째 arm의 각도를 조절한다. 
c, v는 손잡이의 각도를 조절한다. 
좌, 우, 상, 하 방향키는 로봇 팔 전체를 해당 방향으로 움직인다.
스페이스 바를 누르면 손잡이를 벌리거나 오므릴 수 있다.


Mid_solar.py

Tutorial
위성이 1개인 지구, 위성이 2개인 화성이 태양 주위를 공전하고, 각 위성이 행성 주위를 공전한다. 별과 행성, 위성의 자전을 확인할 수 있도록 도형의 중심과 특정 꼭짓점을 이은 선을 추가했다. 좌, 우, 상, 하 방향키는 외계 비행물체를 해당 방향으로 움직인다.

실제 자전, 공전 주기, 각 천체의 크기, 궤도의 반지름 등을 최대한 반영하였다. (다만, 태양의 크기가 굉장히 크고 실제 공전 궤도를 구현하려면 다른 천체가 너무 작아져 눈으로 볼 수 없다는 점을 고려하여 화성의 궤도 반지름과 행성 및 위성의 크기는 임의로 설정하였다.)



Mid_bounceBall.py

Tutorial
좌우 방향키를 꾸욱 누르고 유지하면 공의 위치를 바꿀 수 있다. 방향을 바꾸지 않으면 제자리에서 바닥과 탄성충돌을 한다. 6개의 디딤돌을 올라 마지막 디딤돌에 다다르면 게임 성공이다. 하지만 중간에 떨어지면 패배한다. 점프할 때 소리, 성공 및 패배 시 알맞음 효과음이 나온다.
