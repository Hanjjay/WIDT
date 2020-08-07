def friend(g,who):
  qu = []
  done = set()

  qu.append(who)
  done.add(who)

  while qu:
    p = qu.pop(0)
    print(p)
    for x in g[p]:
      if x not in done:
        qu.append(x)
        done.add(x)


fr_inpo = {
  'Summer' : ['John','Justine','Mike'],
  'John' : ['Summer','Justine'],
  'Justine' : ['John','Summer','Mike','May'],
  'Mike' : ['Summer','Justine'],
  'May' : ['Justine','Kim'],
  'Kim' : ['May'],
  "Moon" : ['Sun'],
  "Sun" : ['Moon']

}
friend(fr_inpo,'Summer')
print()
friend(fr_inpo,'Moon')
