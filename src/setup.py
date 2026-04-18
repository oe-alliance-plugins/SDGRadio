from setuptools import setup
import setup_translate

pkg = 'Extensions.SDGRadio'
setup(name='enigma2-plugin-extensions-sdgradio',
       version='2.0',
       description='Enigma2 Software Defined Radio',
       package_dir={pkg: 'SDGRadio'},
       packages=[pkg],
       package_data={pkg: ['fonts/*.ttf', 'img/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
