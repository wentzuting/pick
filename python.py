import random

# 輸入比賽名稱
tournament_name = input("請輸入比賽名稱: ")

# 輸入選手數量，選擇 4, 8, 16, 32
num_participants = int(input("請選擇選手數量 (4, 8, 16, 32): "))
while num_participants not in [4, 8, 16, 32]:
    num_participants = int(input("無效選擇，請選擇 4, 8, 16 或 32 選手數量: "))

# 輸入選手名稱
participants = []
for i in range(num_participants):
    player_name = input(f"請輸入選手 {i+1} 的名稱: ")
    participants.append(player_name)

# 定義一個字典來存儲每個參賽者的勝場數
standings = {player: 0 for player in participants}

# 定義一個變數來追蹤當前輪數
round_num = 1

# 定義一個函數來更新排行榜
def update_standings(winner, loser):
    standings[winner] += 1
    standings[loser] += 0

# 定義一個函數來顯示排行榜
def display_standings():
    print(f"{tournament_name} 最終排行榜:")
    sorted_standings = sorted(standings.items(), key=lambda x: x[1], reverse=True)
    for rank, (player, wins) in enumerate(sorted_standings, start=1):
        print(f"{rank}. {player} - {wins} 勝")

# 定義一個函數來開始每輪比賽
def start_round():
    global round_num
    # 如果參賽者數量為1則結束比賽
    if len(participants) == 1:
        return None
    
    # 每輪比賽會有一半選手淘汰，將參賽者隨機分組
    random.shuffle(participants)
    matchups = [(participants[i], participants[i+1]) for i in range(0, len(participants), 2)]
    
    # 顯示當前比賽的配對
    for match in matchups:
        print(f"比賽: (A){match[0]} VS (B){match[1]}")
    
    return matchups

# 主程式
while len(participants) > 1:
    # 開始新的一輪
    matchups = start_round()
    if matchups is None:
        break
    
    print("\n請輸入比賽結果 (格式: A 或 B)")

    for match in matchups:
        result = input(f"比賽:(A) {match[0]} VS (B){match[1]} (輸入 'A' 或 'B' 選擇勝者): ")
        
        if result.lower() == 'q':
            break
        
        if result.lower() == 'a' or result.lower() == 'b':
            winner = match[0] if result.lower() == 'a' else match[1]
            loser = match[1] if result.lower() == 'a' else match[0]
            update_standings(winner, loser)
            
            # 淘汰敗者
            participants.remove(loser)
        else:
            print("無效的選擇，請輸入 'A' 或 'B' 來選擇勝者。")
    
    round_num += 1  # 進入下一輪

    if len(participants) == 1:
        print(f"恭喜 {participants[0]} 獲勝！")
        break

# 最終顯示排行榜
display_standings()
