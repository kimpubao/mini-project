#240325 개인 프로젝트 
#주제 _ 블랙잭
#규칙
#1. 카드 2장 이상을 받아 숫자 21을 만드는 게임
#2. 숫자 21을 만든 플레이어 혹은 가까운 플레이어가 이기는 게임
#3. 숫자 21을 넘을 시 패배합니다.
#4. A(Ace)의 숫자는 1 혹은 11을 선택 할 수 있으며 J(JACK) / Q(Queen) / K(King)의 숫자는 10입니다.
#5. 기본으로 카드 2장을 받고 카드를 더 받고 싶은 경우 받을 수 있습니다.

####정확하고 자세한 규칙은 구글 혹은 네이버에 찾아보세요.####

import random

#카드
deck=[]
suits=['hearts','diaomonds','clubs','spades']
ranks=['Ace','1','2','3','4','5','6','7','8','9','Jack','Queen','King']

for suit in suits:
    for rank in ranks:
        deck.append(rank+' of '+suit)

#카드 셔플
def shuffle_deck():
    random.shuffle(deck)
    
#카드 한장 뽑기
def deal_card():
    return deck.pop()

#점수계산
def calculate_hand(hand):
    score = 0
    num_aces = 0
    for card in hand:
        rank=card.split()[0]
        if rank =='Ace': #Ace 카드 점수
            num_aces +=1
            score += 11
        elif rank in ['Jack','Queen','King']: #J/Q/K 점수 설정
            score += 10
        else:
            score += int(rank)
    
    return score

#플레이어 설정하기
def play_game():
    print("블랙잭에 오신 것을 환영합니다 :)")
    shuffle_deck()
    player_hand=[deal_card(), deal_card()]
    dealer_hand=[deal_card(), deal_card()]
    
    while True:
        print('플레이어 카드', player_hand)
        player_score=calculate_hand(player_hand)
        print('플레이어 점수 ', player_score)
        if player_score >21:
            print("플레이어의 카드의 수가 21를 초과하였습니다. 플레이어님께서 패배하셨습니다.")
            return
        elif player_score == 21:
            print("축하드립니다!! 블랙잭 만들었습니다!! ")
            return
        else:
            action=input('카드를 받으시겠습니까?(숫자 1 입력시 카드 받기/숫자 2 입력시 게임결과 보기)')
            if action=='1':
                player_hand.append(deal_card())
            elif action=='2':
                break
#딜러 설정하기
    while True:
        print('딜러 카드', dealer_hand)
        dealer_score=calculate_hand(dealer_hand)
        print('딜러의 점수 ',dealer_score)
        if dealer_score >21:
            print("딜러의 카드의 수가 21를 초과 하였습니다. 플레이어님께서 이기겼습니다.")
            return
        elif dealer_score >=18:
            break
        else:
            dealer_hand.append(deal_card())
#게임 결과 비교
    if player_score > dealer_score:
        print("플레어님께서 이기겼습니다.")
    elif player_score == dealer_score:
        print("플레이어님과 딜러의 점수가 같아 비겼습니다.")
    else:
        print("딜러가 이겼습니다.")

#실행
play_game()
