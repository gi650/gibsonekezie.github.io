
#sync example
def ready_player_one():
    print(
       "This player exists in virtual world that is under attack by robots"
    )

type(ready_player_one)

#async example
async def ready_player_two(score : int):
    print(
       "This player exists in virtual world with callbacks {score}"
    )
type(ready_player_two)