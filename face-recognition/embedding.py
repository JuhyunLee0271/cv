import os, sys, cv2, face_recognition, pickle

class Embedding:

    # To identify the person in the a pickle file, take its name and a unique id as input.
    def __init__(self, name, ref_id):
        self.name = name
        self.ref_id = ref_id
    
    # If the file exists, load to @ref_dict
    def saveRefname(self):
        if os.path.exists("ref_name.pkl"):
            with open("ref_name.pkl", "rb") as f:
                ref_dict = pickle.load(f)
        else:
            ref_dict = dict()
        ref_dict[self.ref_id] = self.name

        with open("ref_name.pkl", "wb") as f:
            pickle.dump(ref_dict, f)

    # Store the embeddings of a particular person in the @embed_dict dictionary use @ref_id of that person as the key.
    # To capture images, press 's' five times. If you want to stop the camera press 'q'
    def saveEmbedVector(self):
        if os.path.exists("ref_embed.pkl"):
            with open("ref_embed.pkl", "rb") as f:
                embed_dict = pickle.load(f)
        else:
            embed_dict = dict()

        for i in range(5):
            key = cv2.waitKey(1)
            cam = cv2.VideoCapture(0)
            while True:
                ret, frame = cam.read()
                cv2.imshow("Capturing", frame)
                small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
                rgb_small_frame = small_frame[:,:,::-1]
                key = cv2.waitKey(1)

                if key == ord('s'):
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    if face_locations != []:
                        face_encoding = face_recognition.face_encodings(frame)[0]
                        if self.ref_id in embed_dict:
                            embed_dict[self.ref_id] += [face_encoding]
                        else:
                            embed_dict[self.ref_id] = [face_encoding]
                        cam.release()
                        cv2.waitKey(1)
                        cv2.destroyAllWindows()
                        break

                elif key == ord('q'):
                    cam.release()
                    cv2.destroyAllWindows()
                    break
        
        with open("ref_embed.pkl", "wb") as f:
            pickle.dump(embed_dict, f)

if __name__ == "__main__":
    embedding = Embedding("Elon Musk", "02")
    embedding.saveRefname()
    embedding.saveEmbedVector()

