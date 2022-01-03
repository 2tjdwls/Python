% 문제 생략
clear all;

cost = 0;
selected_menu = input('주문하실 메뉴를 입력하세요 :');
money = input( '보유하신 금액을 입력하세요 :');

for i = 1 : 1 : size(selected_menu,2)
    
    if ( selected_menu( 1 , i ) == 1 )
        cost = cost + 3000;
    end
    
    if ( selected_menu( 1 , i ) == 2 )
       cost = cost + 1000;
    end
    
    if ( selected_menu( 1 , i ) == 3 )
        cost = cost + 2500;
    end
    
    if ( selected_menu( 1 , i ) == 4 )
        cost = cost + 2000;
    end
    
    if ( selected_menu( 1 , i ) == 5 )
        cost = cost + 3000;
    end
    
     if ( selected_menu( 1 , i ) > 5 )
        '리스트에 없는 메뉴입니다.';
     end
     
end

change = money - cost;

if ( change < 0 )
    disp('보유하신 금액이 부족합니다.');
else
    str = '거스름돈은 %d원 입니다.';
    sprintf( str , change )
end