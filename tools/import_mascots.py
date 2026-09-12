"""Use the user's transparent PNGs unchanged; derive WebP for web delivery."""
from pathlib import Path
from PIL import Image
import shutil,json,argparse
parser=argparse.ArgumentParser(description='Import the supplied transparent mascot PNGs from a folder.')
parser.add_argument('source',type=Path,help='Folder containing the original UUID-named PNG uploads')
args=parser.parse_args()
R=Path(__file__).resolve().parents[1];U=args.source;D=R/'assets/img/mascot'
mapping={
'urban-neutral':'22746695-eb4b-46a2-a58b-ab2fe351c1d1',
'urban-wave':'84b28262-05fa-4a74-8325-9527ee33930e',
'urban-point':'33946b0e-fa4b-42fc-8cef-6a5c257a7ea2',
'urban-work':'49b8fa1c-fdff-4f67-b273-ed24856c0078',
'urban-present':'8a4245f3-d54b-4abd-80cd-7eddaee876e2',
'urban-think':'87be3a93-3d61-47e3-b1d9-338efc0cb235',
'urban-idea':'9da27910-c28e-46f6-ad3b-9abf47cd10d8',
'urban-tablet':'c2fb2f54-5a23-4070-8ace-e16fb39ecd72',
'urban-float':'4a7c3cef-b4bd-4749-9fe7-4fe1970cd0fc',
'urban-rest':'62f3421f-47e6-4906-8f9e-05e62c57693b',
'urban-celebrate':'3610b6f9-631a-4d18-9d47-ae80baeb99be',
'urban-crouch':'c5eb640b-46e5-4f4d-97bb-70f175737fe6',
'workshop-vase':'f8ba8b3c-50ba-4e31-953b-d4295199b6ab',
'workshop-wave':'5cc8cf70-34d7-4b71-9abb-8d446ceb88fd',
'workshop-sit':'407da5f9-7dd0-4946-956d-d392338f5028'}
for pose,name in mapping.items():
    p=U/(name+'.png');im=Image.open(p);assert im.mode=='RGBA' and im.getchannel('A').getextrema()[0]==0
    shutil.copyfile(p,D/(pose+'.png'));im.save(D/(pose+'.webp'),quality=92,method=6)
    print(pose,flush=True)
(D/'sources.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2))
print('15 poses imported. Duplicate upload intentionally retained in original uploads only.')
