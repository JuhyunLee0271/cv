import face_recognition, cv2, glob, pickle
import numpy as np

class Recognition:

    def __init__(self):
        with open("ref_name.pkl", "rb") as f:
            self.ref_dict = pickle.load(f)
        with open("ref_embed.pkl", "rb") as f:
            self.embed_dict = pickle.load(f)
        
        self.known_face_encodings = []
        self.known_face_names = []

        for ref_id, embed_list in self.embed_dict.items():
            for embed in embed_list:
                self.known_face_encodings += [embed]
                self.known_face_names += [ref_id]
    
    def run(self):
        cam = cv2.VideoCapture(0)
        
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            ref, frame = cam.read()
            small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:,:,::-1]

            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                    face_names.append(name)
            process_this_frame = not process_this_frame

            for (top_s, right, bottom, left), name in zip(face_locations, face_names):
                top_s *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top_s), (right, bottom), (0,0,255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0,0,255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, self.ref_dict[name], (left+6, bottom-6), font, 1.0, (255, 255, 255), 1)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.imshow("video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    recognition = Recognition()
    recognition.run()