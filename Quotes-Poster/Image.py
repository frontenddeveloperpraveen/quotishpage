quotes = [ 'If you are not willing to risk the usual, you will have to settle for the ordinary.', 'To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.', "Life is what happens when you're busy making other plans.", 'The best revenge is massive success.', "In three words I can sum up everything I've learned about life: it goes on.", 'Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.', "I have not failed. I've just found 10,000 ways that won't work.", 'Be yourself; everyone else is already taken.', 'It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change.', 'The journey of a thousand miles begins with a single step.', 'The future belongs to those who believe in the beauty of their dreams.', 'Do not wait to strike till the iron is hot, but make it hot by striking.', "You miss 100% of the shots you don't take.", 'If you want to achieve greatness stop asking for permission.', "It always seems impossible until it's done.", 'The purpose of our lives is to be happy.', "Don't count the days, make the days count.", 'Success usually comes to those who are too busy to be looking for it.', 'Success is not final, failure is not fatal: It is the courage to continue that counts.', 'The only way to achieve the impossible is to believe it is possible.', 'Happiness is not something ready made. It comes from your own actions.', 'Strive not to be a success, but rather to be of value.', 'Change your thoughts and you change your world.', 'Whatever you are, be a good one.', "Your time is limited, don't waste it living someone else's life.", 'Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.', 'The best way to predict the future is to create it.', 'The only way to do great work is to love what you do.', 'The only thing we have to fear is fear itself.', "Don't watch the clock; do what it does. Keep going.", 'Success is not how high you have climbed, but how you make a positive difference to the world.', 'It is during our darkest moments that we must focus to see the light.',"Believe you can and you're halfway there.", 'The only limit to our realization of tomorrow will be our doubts of today.', 'The best way to predict the future is to invent it.', "You don't have to be great to start, but you have to start to be great."]
import cv2;
import textwrap;
def put_text(img, text, x_value, y_value):
    font = cv2.FONT_HERSHEY_SIMPLEX
    wrapped_text = textwrap.wrap(text, width=22)
    x, y = 200, 40
    font_size = 2
    font_thickness = 3

    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]
        gap = textsize[1] + 40
        y = y_value + i * gap
        #y = int((img.shape[0] + textsize[1]) / 2) + i * gap
        x = int((img.shape[1] - textsize[0]) / 2)
        cv2.putText(img, line, (x_value, y), font,
                    font_size,
                    (255,255,255),
                    font_thickness,
                    lineType = cv2.LINE_AA)

for idx, i in enumerate(quotes):
    idx+=1
    img = cv2.imread("./Assets/Images/1.png")
    put_text(img,i , 131, 385)
    if(len(i) > 40):
        i = i[0:40]
    if(idx < 10):
        idx = str(0)+str(idx)
    location = f"Output/Images/{str(idx)} - {i}.jpg"
    cv2.imwrite(location, img)

else:

    print("Process Completed")