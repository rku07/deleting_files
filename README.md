# delete_files

**Dependencies**
* argparse
* subprocess

***Run the following command***
> py files_delete.py --p /path/to
> * Will delete the files older than 7 days (default)

> py files_delete.py --p /path/to --d 5
>  * Will delete the files older than 5 days (passed through --d argument)



* --p : path of the directory
* --d : days to consider for deletion

**OUTPUT**

* List of files deleted and Done
* Some Issue, if something fails
