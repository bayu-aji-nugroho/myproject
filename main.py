
from manim import Scene,Circle,Create,Square,BLUE,PURPLE,Transform,FadeOut,Text,Tex


class mainV(Scene):
    
    dataText = [
       r"$\frac{\cos t - \cos 3t}{\sin t + \sin 3t} = \tan t $",
       r"$ \frac{\cos t - (\cos 2t\cos t - \sin 2t\sin t)}{ \sin t + \sin 2t\cos t + \cos 2t\sin t} = \tan t $",
       r"$ \frac{\cos t - (cos^3 t- \sin^2 t\cos t- 2sin^2 t\cos t)}{\sin t +2\sin t\cos^2 t + cos^2 t\sin t -sin^3 t} = \tan t $",
       r"$ \frac{\cos t -\cos^3 t+ \sin^2 t\cos t+ 2sin^2 t\cos t}{\sin t +2\sin t\cos^2 t + cos^2 t\sin t -sin^3 t} = \tan t $",
       r"$\frac{\cos t -\cos^3t +3\sin^2 t\cos t}{\sin t -\sin^3 t +3 \cos^2 t\sin t} = \tan t $",
       r"$\frac{\cos t(1-\cos^2 t +3\sin^2 t)}{\sin t(1-sin^2 t +3\cos^2 t)} = \tan t $",
       r"$\frac{\sin t+3\sin t}{\cos t +3\cos t} = \tan t $",
       r"$\frac{\sin t}{\cos t} = \tan t$",
       r"$\tan t = \tan t $"
    ]
    def construct(self):
        for i in range(len(self.dataText)):
            if i == 0:
                mainText = (Tex(self.dataText[i]))
                self.play(Create(mainText))
                self.wait(1)
            try: 
                text2 = (Tex(self.dataText[i+1]))
            except IndexError:
                self.play(FadeOut(mainText))
                break
            self.play(Transform(mainText,text2))
            self.wait(1)
            text2 = mainText
            
            