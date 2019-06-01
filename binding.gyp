{
  'targets': [
    {
      'target_name': 'exiv2',
      'sources': [
        'exiv2node.cc'
      ],
      'include_dirs' : [
        '<!@(pkg-config --variable=includedir exiv2)',
        "<!(node -e \"require('nan')\")"
      ],
      'xcode_settings': {
        'MACOSX_DEPLOYMENT_TARGET': '10.12',
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'OTHER_CPLUSPLUSFLAGS': [
            '-stdlib=libc++',
            '-fcxx-exceptions',
            '-frtti',
            '-fexceptions'
        ],
      },
      "cflags": [
        "-Wdeprecated-declarations",
        "-fexceptions",
        "-frtti"
      ],
      'cflags_cc': [
        '-fexceptions',
        "-frtti",
        "-Wdeprecated-declarations"
      ],
      'libraries': [
        "-Wl,-rpath,./build/Release/exiv2.a"    ,
        '<!@(pkg-config --libs exiv2)'
      ]
    }
  ]
}
