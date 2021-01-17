from speech_to_text import *
from video2keyframes import *

def video2recipe(video_id, videopath):
    dir = './extract_result/'
    keyframes, time_frame_list = keyframs_time(videopath, dir)
    transcript_list = get_text_from_video(video_id)
    temp_text = ""
    counter = 1

    divided_steps = divide_steps(transcript_list, time_frame_list)
    for step, keyframe in zip(divided_steps,keyframes):
        #        print("This is step: " + str(counter))
        #       print(step)
        counter += 1
        keyframe["transcript"] = step
    for item in transcript_list:
        text = item['text']
        temp_text += text

        # result = classify_content(temp_text)
    ingredients_result = []
    equipments_result = []
    ingredients = []
    equipments = []
    temp_result = analyze_entity_sentiment(temp_text)
    # Remove duplicates
    [ingredients.append(x) for x in temp_result if x not in ingredients]
    [equipments.append(x) for x in temp_result if x not in equipments]
    # final filtering
    for item in ingredients:
        if item in ingredients_list:
            ingredients_result.append(item)
    for item in equipments:
        if item in equipment_list:
            equipments_result.append(item)
    for t, s in zip(res, ingredients_result):
        t["transcript"] = s
    res = {"ingredients_result": ingredients_result,
           "equipments_result":equipments_result,
           "steps": keyframes}
    return res



res = video2recipe("ztl0gGVFoK0&t", 'demo.mp4')
print(res)