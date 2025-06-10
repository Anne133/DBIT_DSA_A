def countdown_head(n):
    if n < 0:
        return
  
    countdown_head(n - 1)
    print(n)


countdown_head(7)