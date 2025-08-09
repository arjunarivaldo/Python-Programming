from IPython.terminal.shortcuts.filters import pass_through

hero1 = 'Zilong'
hero2 = 'Roger'
hero3 = 'Gusion'



def attack():
        enemy_remain = 10

        while (enemy_remain > 0):
            if enemy_remain > 0:
              print ('Jumlah musuh masih ada: ', enemy_remain)
              enemy_remain = enemy_remain - 1
              print(f'{hero3} mengalahkan 1 musuh')
            if enemy_remain == 0:
              print(f'\nSemua musuh telah dikalahkan oleh {hero3}')