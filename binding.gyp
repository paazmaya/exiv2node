{
  'targets': [
    {
      'target_name': 'exiv2',
      'sources': [
        'exiv2node.cc'
      ],
      'include_dirs' : [
        "vendor/exiv2-0.25/include",
        "<!(node -e \"require('nan')\")"
      ],
      "libraries": [ "-Wl,-rpath,./build/Release/exiv2.a" ],
      'xcode_settings': {
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'OTHER_CPLUSPLUSFLAGS': ['-stdlib=libc++','-fcxx-exceptions', '-frtti'],
      },
      "cflags": [ 
        "-Wdeprecated-declarations"
      ],
      'cflags_cc': [
        '-fexceptions'
      ],
      "dependencies": [
        "vendor/exiv2.gyp:XMPSDK",
        "vendor/exiv2.gyp:libexiv2"
      ]
    }
  ]
}
