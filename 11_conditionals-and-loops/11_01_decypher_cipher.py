# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2349h30023388281e3299371l1l3094842o0333322883"
for c in secret:
  if c not in ['0','1','2','3','4','5','6','7','8','9']:
    print(c)

