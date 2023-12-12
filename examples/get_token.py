import config
import htb


config = config.Config()
print(config.email)

htb = htb.HTB()
htb.get_token(config.email, config.password)
