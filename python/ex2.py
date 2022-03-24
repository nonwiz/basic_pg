# Problem 2, Story telling


input_list = ['title', 'protagonist', 'secondary',  'secondary_wish', 'protagonist_statement', 'scenario'] 


input_dict = dict()

story = """
title
protagonist had always loved old-fashioned scenario with its heavy, harsh hills. It was a place where protagonist felt relaxed. protagonist was a malicious, funny, brandy drinker with beautiful eyes and spiky fingers. protagonist friends saw protagonist as a confused, colossal coward. Once, protagonist had even helped a petite deaf person cross the road. That's the sort of man protagonist was. protagonist walked over to the window and reflected on protagonist picturesque surroundings. The hail pounded like partying aardvarks. Then protagonist saw something in the distance, or rather someone. It was the figure of secondary. secondary was a caring wally with tall eyes and charming fingers. protagonist gulped. protagonist was not prepared for secondary. As protagonist stepped outside and secondary came closer, protagonist could see the curried smile on protagonist face. \"Look protagonist,\" growled secondary, with a thoughtless glare that reminded protagonist of caring aardvarks. \"It's not that I don't love you, but I want secondary_wish. You owe me 4978 euros.\" protagonist looked back, even more angry and still fingering the giant knife. \"secondary, protagonist_statement,\" protagonist replied. They looked at each other with sneezy feelings, like two sad, stingy snakes jumping at a very ruthless bar mitzvah, which had indie music playing in the background and two kind uncles shouting to the beat. protagonist regarded secondary's tall eyes and charming fingers. \"I don't have the funds ...\" protagonist lied. secondary glared. \"Do you want me to shove that giant knife where the sun don't shine?\" protagonist promptly remembered protagonist malicious and funny values. \"Actually, I do have the funds,\" protagonist admitted. protagonist reached into protagonist pockets. \"Here's what I owe you.\" secondary looked surprised, protagonist wallet blushing like a rabblesnatching, racid ruler. Then secondary came inside for a nice glass of brandy. THE END 
"""

for item in input_list:
   user_input = str(input(f"\n{item}: "))
   story = story.replace(item, user_input)


print(story)
