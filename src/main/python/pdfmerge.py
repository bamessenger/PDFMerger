import sys
import os.path

from PyPDF2 import PdfFileMerger, PdfFileReader

class ExecutePDF:
    def merge(self, fileCopy, fileInsertInto, pageStart, pageIteration):
        # Increase system recursion limit to compensate for larger files
        sys.setrecursionlimit(2000)
        # Loop through each file chosen by user
        for files in range(len(fileInsertInto)):
            page = pageStart
            mergedObject = PdfFileMerger()
            pageCount = PdfFileReader(fileInsertInto[files]).getNumPages()
            mergedObject.append(fileInsertInto[files], import_bookmarks=False)
            # Iterate through each file based on user page iteration input
            while page < pageCount:
                mergedObject.merge(position=page, fileobj=fileCopy,
                                   pages=(0, 2), import_bookmarks=False)
                page = page + pageIteration
            # Write all the files into a file which is named as shown below
            # File directory is that of the last insert into file chosen
            directory = os.path.dirname(fileInsertInto[-1])
            mergedObject.write(os.path.splitext(fileInsertInto[
                files])[0]+"_MERGED.pdf")
            # reset system recursion limit back to system default
            sys.setrecursionlimit(1000)
            mergedObject.close()