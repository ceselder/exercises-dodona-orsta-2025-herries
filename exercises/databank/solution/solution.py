def insert_video(databank, video):
  nieuwe_viewcount = video[1]
  ingevoegd = False
  for i, (naam, viewcount) in enumerate(databank):
    if nieuwe_viewcount < viewcount:
      databank.insert(i, video)
      ingevoegd = True
      break
  
  if not ingevoegd:
    databank.append(video)
  print(databank)