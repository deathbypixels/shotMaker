import os
import nuke


# Feel free to use and change this script to match your needs,
# the author isn't responsible for any damage made by the script

def makeFolders():
    # Checks if Project Directory is Set
    if nuke.Root()['project_directory'].value() == '':
        nuke.message('Error: <span style="color:red">Set Project Directory</span>')
    else:

        # Defines all Folder Names
        rt = nuke.Root()['project_directory'].value()
        prj = 'projects'
        lut = 'luts
        r = 'renders'
        sc = 'scripts'
        shw = 'show'
        ep = 'episode'
        sq = 'seq'
        ip = 'in'
        op = 'out'
        sht = 'shot'
        col = 'color'
        cc = 'cc'
        ocio = 'ocio''
        elm = 'elements'
        fnt = 'fonts'
        pnt = 'paint'
        ref = 'ref'
        rto = 'roto'
        prndr = 'prerender'
        qt  = 'quicktimes'
        ae = 'ae'
        moc = 'mocha'
        nk = 'nuke'
        sil = ' silhouette'
        syn = 'syntheyes'

        # Combines Folders with Project Directory




        fldr1 = rt + r
        fldr2 = rt + s
        fldr3 = rt + TWDR
        fldr4 = rt + THDR
        fldr5 = rt + ST
        fldr6 = rt + F

        # Prints for Debugging
        print fldr1
        print fldr2
        print fldr3
        print fldr4
        print fldr5
        print fldr6

        # Generates Folders
        if not os.path.exists(fldr1):
            os.makedirs(fldr1)
        if not os.path.exists(fldr2):
            os.makedirs(fldr2)
        if not os.path.exists(fldr3):
            os.makedirs(fldr3)
        if not os.path.exists(fldr4):
            os.makedirs(fldr4)
        if not os.path.exists(fldr):
            os.makedirs(fldr)
        if not os.path.exists(fldr6):
            os.makedirs(fldr6)

        nuke.message('Folders Generated')


pass
