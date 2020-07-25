spell = "Wingardium Leviosa"
sub = input()

if sub in spell:
    print(spell.find(sub))
else:
    print(-1)
