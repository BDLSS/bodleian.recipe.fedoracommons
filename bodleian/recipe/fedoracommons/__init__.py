# -*- coding: utf-8 -*-

import glob
import os
import shutil
import subprocess
import zipfile
import zc.buildout

from hexagonit.recipe.download import Recipe as downloadRecipe

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.options = options
        options.setdefault('target', os.path.join(buildout['buildout']['directory'], 'lib', name))
        self.download = downloadRecipe(buildout, name, options)

    def install(self):
        """Installer"""
        options = self.options
        # we get the pom.xml from the buildout conf/ dir
        pom_path = os.path.join(os.getcwd(), 'conf')

        # If a path to the zip file is not provided, then download it and build it
        if not 'zip' in options:
            output = self.download.install()
            os.chdir(output[1])
            # this is where maven expects the pom.xml file
            dest_path = output[1]
            # import pdb;pdb.set_trace()
            # we move it into req destination
            print 'moving pom.xml to ', os.path.join(dest_path, 'pom.xml'), '*****'
            shutil.move(os.path.join(pom_path, 'pom.xml'), os.path.join(dest_path, 'pom.xml'))

            # Call Maven to build couchdb-lucene
            subprocess.call(['mvn', 'install'])
            try:
            #    import pdb;pdb.set_trace()
                options['zip'] = glob.glob(os.path.join(options['target'], 'target', '*.zip'))[0]
            except IndexError:
                raise zc.buildout.UserError('Maven failed')
        # Create directory for extracted files
        target_dir = options['target']

        # Temporary directory
        tmp_dir = '/tmp/'
        # Unzip the produced archive
        with zipfile.ZipFile(options['zip']) as zip_file:
            # Extract
            zip_file.extractall(tmp_dir)
            # Find the run member
            run_member = next(_ for _ in zip_file.namelist() if _.endswith('run'))
            run_path = os.path.join(tmp_dir, run_member)

            # Make the extracted run file executable
            os.chmod(run_path, 0777)
            # Move from the tmp directory to the target directory
            shutil.move(os.path.join(tmp_dir, zip_file.namelist()[0][:-1]), target_dir)
        return [target_dir]

    def update(self):
        pass

