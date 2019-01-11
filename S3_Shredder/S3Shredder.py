import boto3 as boto

s3 = boto.resource("s3")
s3Client = boto.client("s3")
s3Keys = dict()


def listBuckets():
    for bucket in s3.buckets.all():
        print(bucket.name)

def rmObjects(bucket, objects):
    '''
    This function deletes all of the S3 keys passed to it in the objects param
    :param bucket: name of an S3 bucket
    :param objects: a representation of one or more S3 Objects, a boto s3 class
    '''
    print("{} keys will be removed, are you sure?".format(len(objects)))
    dispose = input("Y/N...").upper()
    if dispose == "Y":

        for obj in objects:
                try:
                    name = obj['Key']
                    shredder = s3.Object(bucket,obj['Key'])
                    shredder.delete()
                    print("POW! Deleted {}".format(name))
                except:
                    print("something failed")
    else:
        return


if __name__ == "__main__":
    while True:
        print('\n\n**************************************\nWelcome to S3 Shredder.\n \
a utility for bulk-deleting S3 objects .... \n\n "Sayonara you shell-backed simpletons" \n\n')

        print('OPTIONS: \n \
              1. List your buckets \n \
              2. Delete some shit \n \
              Q to Quit ')
        choice = input("")
        if choice == '1':
            listBuckets()
            continue
        elif choice.upper() == 'Q':
            break
        elif choice != '2':
            continue
        else:
            buckName = input("enter a bucket name or Q to quit... ")
            if buckName.upper() == 'Q':
                break
            else:
                prefix = input("enter a prefix ... ") # deletes all keys in the prefix and all nested prefixes up to 1000 keys

                s3Keys = s3Client.list_objects_v2(Bucket=buckName,Prefix=prefix)
                s3Objects = s3Keys['Contents']  # a list of dictionaries
                for obj in s3Objects:
                    print("{}/{}".format(buckName,obj['Key']))
                disposition = input("Do you want to remove all of these objects? Y/N").upper()
                if disposition =="Y":
                    rmObjects(buckName, s3Objects)
                    continue
                else:
                    continue
