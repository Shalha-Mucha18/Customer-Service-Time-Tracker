import cv2

# Load the  video file
video_path = "C:/Users/ASUS/Desktop/Service Time/fringestorez.mp4"  
cap = cv2.VideoCapture(video_path)

# initialize the background subtractor for detecting motion
back_sub = cv2.createBackgroundSubtractorMOG2()

# Customer tracking data
customers = {}
customer_id = 0
customer_times = []

# Sampling rate (process every nth frame)
frame_sampling_rate = 5
frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # frame counter
    frame_number += 1

    # Process nth frame
    if frame_number % frame_sampling_rate != 0:
        continue

    # Resize frame 
    frame = cv2.resize(frame, (320, 180))

    # apply subtraction
    fg_mask = back_sub.apply(frame)

    # find moving objects
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # filter out  area
        if cv2.contourArea(contour) < 500:
            continue

        # get bounding box for the detected object
        x, y, w, h = cv2.boundingRect(contour)
        center_x, center_y = x + w // 2, y + h // 2

        # check for the new customer
        matched = False
        for cid, data in customers.items():
            cx, cy, start_frame = data
            if abs(center_x - cx) < 50 and abs(center_y - cy) < 50:
                # update  position
                customers[cid] = (center_x, center_y, start_frame)
                matched = True
                break

        if not matched:
            # new customer 
            customers[customer_id] = (center_x, center_y, frame_number)
            customer_id += 1

    # check if any customer has been stationary long enough 
    to_remove = []
    for cid, data in customers.items():
        cx, cy, start_frame = data
        if frame_number - start_frame > (16 * 59.94) / frame_sampling_rate:
            customer_times.append((frame_number - start_frame) * frame_sampling_rate / 59.94)
            to_remove.append(cid)

    for cid in to_remove:
        del customers[cid]

cap.release()

# calculate the average service time
if customer_times:
    average_time = sum(customer_times) / len(customer_times)
    print(f"Average service time: {average_time:.6f} seconds")
else:
    print("No customers were detected.")