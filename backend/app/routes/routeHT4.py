# Import packages
from fastapi import File, UploadFile
from fastapi import APIRouter

# Local import
from ..ec2.ht4 import uploadImageToS3Bucket
# router
router = APIRouter(
  prefix="/ht4",
  tags=["ht4"],
  responses={404: {"description": "Not found"}},
)

# endpoint to upload a image
@router.post("/upload-file/")
async def create_upload_file(file: UploadFile = File(...)):
  if not file:
    return {"status": "error", "message": "No file"}
  else:
    # upload file to S3
    response =  uploadImageToS3Bucket(file.file, file.filename)
    # return the url of the file
    return {"status": "success", "message": "File uploaded", "url": f"https://202109567.s3.amazonaws.com/{file.filename}"}
  