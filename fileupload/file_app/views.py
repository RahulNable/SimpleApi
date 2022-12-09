from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from bs4 import BeautifulSoup
import zipfile
import os
from django.http import JsonResponse
from rest_framework.decorators import api_view
from os import listdir
from os.path import isfile
import shutil
from file_app.models import TenderImport, File
from fileupload.settings import IMAGEFILE
import pandas as pd

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    print('request.data ', request.data.get("file"))

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def toDataBase(request):

    with open(IMAGEFILE, 'rb') as file:
        binaryData = file.read()

    tender = TenderImport.objects.create(CustomerRefNo = 102, Refno = 22, Image = binaryData, DESCRIPTION = 'some description', UNIT = 'nos', Quantity = 22, Rate = 52, Amount = 1200,)
    print('CreatedInTenderImport>>>>',tender)

    return JsonResponse({'output': "hello"})


@api_view(['GET'])
def getFileNames(request):

    filenames = []

    for f in listdir('./mediafiles'):
        if isfile(f'./mediafiles/{f}'):
            filenames.append({
                "filename": f
            })
            print(f)
    return JsonResponse({"filenames": filenames})


@api_view(['POST'])
def extractFile(request):

    filename = request.data.get('filename')
    print('request=========>', filename)

    # remove old extracted files
    if os.path.exists("./mediafiles/ExtractedExcelfile/"):
        print('Deleting...Deleting...Deleting...Deleting...Deleting...Deleting...')
        shutil.rmtree("./mediafiles/ExtractedExcelfile/")
        print('Deleted   Deleted   Deleted   Deleted   Deleted   Deleted   ')

    with zipfile.ZipFile(f'./mediafiles/{filename}', 'r') as zip_ref:
        zip_ref.extractall('./mediafiles/ExtractedExcelfile/')

    files = os.listdir('./mediafiles/ExtractedExcelfile/xl/drawings')

    randomfilename = filename.replace('.xlsx','_')

    i = 0
    for file in files:

        i = i + 1
        imageData = []
        if file:
            if file == f'drawing{i}.xml': 
                print(file)
                selectedFile = f'drawing{i}.xml'

                # Reading the data inside the xml file to a variable under the name  data
                with open(f'./mediafiles/ExtractedExcelfile/xl/drawings/drawing{i}.xml', 'r') as f:
                    data = f.read() 

                print(f'inside file {selectedFile}:')

                # Passing the stored data inside the beautifulsoup parser 
                bs_data = BeautifulSoup(data, 'xml') 


                def extractText_FromRow(inputText):
                    print('inside row function')
                    # print(inputText)

                    sub1 = "<xdr:row>"
                    sub2 = "</xdr:row>"

                    idx1 = inputText.index(sub1)
                    idx2 = inputText.index(sub2)

                    res = ''
                    for idx in range(idx1 + len(sub1), idx2):
                        res = res + inputText[idx]
                    return res
                    # print('extracted text',res)
                def extractText_FromColumn(inputText):
                    print('inside column function')

                    sub1 = "<xdr:col>"
                    sub2 = "</xdr:col>"

                    idx1 = inputText.index(sub1)
                    idx2 = inputText.index(sub2)

                    res = ''
                    for idx in range(idx1 + len(sub1), idx2):
                        res = res + inputText[idx]
                    return res

                def extract_imagename(inputText):
                    print('inside extract_imagename function')

                    sub1 = 'name="'
                    sub2 = '.png"'

                    # idx1 = inputText.index(sub1)
                    # idx2 = inputText.index(sub2)

                    idx1 = inputText.index(sub1)

                    if '.png"' in y:
                        idx2 = y.index(sub2)
                    else:
                        sub2 = '.jpg"'
                        idx2 = y.index(sub2)
                    
                    res = ''
                    for idx in range(idx1 + len(sub1), idx2):
                        res = res + inputText[idx]
                    # return res
                    return res + sub2.replace('"','')
                    # print('extracted text',res)

                # imageData = []

                x = bs_data.find_all(['xdr:oneCellAnchor'])

                for y in x:
                    y = str(y)
                    # print(y)

                    if 'col' in y:
                        colValue = extractText_FromColumn(y)

                    if 'row' in y:
                        rowValue = extractText_FromRow(y)

                    if 'image' in y:                     
                        imageName = extract_imagename(y)

                    imageName = "".join([randomfilename, imageName])
                    print(colValue, rowValue, imageName)
                    
                    imageData.append({
                        "col": colValue,
                        "row": rowValue,
                        "imagename": imageName
                    })


                print(f'imageData for file {selectedFile}', imageData)
                print('-----------------------------------------------------------')

            files = os.listdir('./mediafiles/ExtractedExcelfile/xl/media/')
            # print('files------------------------>',files)
            for file in files:
                print(file)
                os.rename(f'./mediafiles/ExtractedExcelfile/xl/media/{file}', f'./mediafiles/ExtractedExcelfile/xl/media/{"".join([randomfilename, file])}')
            
            # code for database
            # flag = 0
            # df = pd.read_excel(f'./mediafiles/{filename}')
            # rows = df.values.tolist()
            # for row in range(10):
            #     flag = 0
            #     for col in range(7):
            #         for imageDataIndex in imageData:
            #             # print(row,imageDataIndex['row'],col,imageDataIndex['col'])
            #             if row == int(imageDataIndex['row']) and col == int(imageDataIndex['col']):
            #                 # print(row,imageDataIndex['row'],col,imageDataIndex['col'])
            #                 print('row = ',row,'========image in this row============')
            #                 print(rows[row-1][0], rows[row-1][1], rows[row-1][2], rows[row-1][4], rows[row-1][5], rows[row-1][6], rows[row-1][7])
            #                 flag = 1
            #                 with open(f'./mediafiles/ExtractedExcelfile/xl/media/{imageData[imageDataIndex].imagename}', 'rb') as file:
            #                     binaryData = file.read()

            #                 tender = TenderImport.objects.create(CustomerRefNo = rows[row-1][0], Refno = rows[row-1][1], Image = binaryData, DESCRIPTION = rows[row-1][2], UNIT = rows[row-1][4], Quantity = rows[row-1][5], Rate = rows[row-1][6], Amount = rows[row-1][7])
            #                 print('CreatedInTenderImport>>>>',tender)
            #     if flag == 0:
            #         print('row = ',row,'========no image in this row============')
            #         print(rows[row-1][0], rows[row-1][1], rows[row-1][2], rows[row-1][4], rows[row-1][5], rows[row-1][6], rows[row-1][7])
            #         tender = TenderImport.objects.create(CustomerRefNo = rows[row-1][0], Refno = rows[row-1][1], DESCRIPTION = rows[row-1][2], UNIT = rows[row-1][4], Quantity = rows[row-1][5], Rate = rows[row-1][6], Amount = rows[row-1][7])
            #         print('CreatedInTenderImport>>>>',tender)
                            
        
            return JsonResponse({"filename": filename,"imagedata": imageData})
    # return JsonResponse({"filename": filename})

