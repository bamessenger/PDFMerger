import math
import os.path

from pdfrw import PdfWriter, PdfReader, PageMerge


class ExecutePDF:
    def merge(self, fileCopy, fileInsertInto, pageStart, pageIteration):
        readerCopy = PdfReader(fileCopy)
        page = pageStart - 1
        pages = 0
        pageIterate = pageIteration
        writer = PdfWriter()
        currentPage = 0
        copyFrom_totalPages = len(PdfReader(fileCopy).pages)
        # Loop through each file chosen by user
        for files in range(len(fileInsertInto)):
            # Read object for fileInsertInto file(s)
            readerIns = PdfReader(fileInsertInto[files])
            # Calculate the total pages for the current fileInsertInto file
            insInto_totalPages = len(PdfReader(fileInsertInto[files]).pages)
            # Calculate total number of pages upon merging...round up to nearest
            # whole number
            totalPages = math.ceil((insInto_totalPages + ((insInto_totalPages -
                                                pageStart)/pageIterate) *
                                               copyFrom_totalPages))
            while pages < totalPages:
                if pages == page:
                    writer.addpages(readerCopy.pages)
                    page += pageIterate
                    pages += copyFrom_totalPages
                else:
                    writer.addpage(readerIns.pages[currentPage])
                    currentPage += 1
                    pages += 1
            # Write all the files into a file which is named as shown below
            # File directory is that of the last insert into file chosen
            directory = os.path.dirname(fileInsertInto[-1])
            writer.write(
                os.path.splitext(fileInsertInto[files])[0] + "_MERGED.pdf")