import Leap, sys, thread, time
from Leap import CircleGesture,KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapMotionListener(Leap.Listener):
	finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
	bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
	state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']


	def on_init(self, controller):
		print "Initialized"


	def on_connect(self, controller):
		print "Motion Sensor Connected!"

		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);



	def on_disconnect(self, controller):
		print "Motion Sensor Disconnected"



	def on_exit(self, controller):
		print "Exited"


	def on_frame(self, controller):
		frame = controller.frame()
		frameID = str(frame.id)
		frameTS = str(frame.timestamp)
		frameHands = len(frame.hands)
		frameHands = str(frameHands)
		frameFingers = len(frame.fingers)
		frameFingers = str(frameFingers)
		frameTools = len(frame.gestures())
		frameTools = str(frameTools)
		frameGestures = len(frame.gestures())
		frameGestures = str(frameGestures)

		"""print "Frame ID:  " +  str(frame.id) \
		 + " Timestamp" + str(frame.timestamp) \
		 + " Number of hands: " + frameHands \
		 + " Number of fingers: " + frameFingers \
		 + " Number of tools: " + frameTools \
		 + " Number of gestures: " + frameGestures"""

		for hand in frame.hands:
		 	'''handType = "Left Hand" if hand.is_left else "Right Hand"

		 	print handType + " Hand ID: " + str(hand.id) + " Palm Position: " + str(hand.palm_position)

		 	normal = hand.palm_normal
		 	direction = hand.direction

		 	print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw + Leap.RAD_TO_DEG)

		 	arm = hand.arm
		 	print "Arm Direction: " + str(arm.direction) + " Wrist Position: " + str(arm.wrist_position) + " Elbow Position " + str(arm.elbow_position)'''

		 	for finger in hand.fingers:
		 		fingerType = finger.type
		 		fingerWidth = str(finger.width)
		 		fingerLength = str(finger.length)
		 		fingerID = str(finger.id)

		 		print "Type: " + self.finger_names[fingerType] \
		 		+ " ID: " + fingerID \
		 		+ " Length " + fingerLength \
		 		+ " Width (mm): " + fingerWidth

		 		for b in range(0,4):
		 			bone = finger.bone(b)
		 			print "Bone: " + self.bone_names[bone.type] + " Start: " + str(bone.prev_joint) + " End: " + str(bone.next_joint) + " Direction: " + str(bone.direction)

def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()

	controller.add_listener(listener)

	print "Press enter to quit"
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)


if __name__ == "__main__":
	main()