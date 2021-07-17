print ("What type of cover does the book have? (soft or hard)")
book_type = input ()
if (book_type == "soft"):
  print ("is the book perfect bound?")
  book = input()
  if (book == "yes"):
    print ("Soft cover, perfect bound books are very popular!")
  else:
    print ("Soft covers with coils or stitches are great for short books")
if (book_type == "hard"):
  print ("Books with hard covers can be more expensive!")