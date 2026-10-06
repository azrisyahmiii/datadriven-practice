def dice_roll_scoring(dice: list[int]):
  
  freq = {}
  for d in dice:
    freq[d] = freq.get(d, 0) + 1
    
  counts = sorted(freq.values(), reverse=True)
  
  if counts[0] == 5:
    return 50
  if counts[0] == 4:
    return 40
  if counts == [3,2]:
    return 25
  else:
    return sum(dice)  
