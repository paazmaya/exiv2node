{
  'targets': [
    {
      'target_name': 'XMPSDK',
      "type": "static_library",
      "include_dirs": [
        'exiv2-0.25/xmpsdk/include/'
      ],
      "sources": [
        "exiv2-0.25/xmpsdk/src/XML_Node.cpp",
        "exiv2-0.25/xmpsdk/src/XMPMeta.cpp",
        "exiv2-0.25/xmpsdk/src/XMPMeta-GetSet.cpp",
        "exiv2-0.25/xmpsdk/src/XMPMeta-Parse.cpp",
        "exiv2-0.25/xmpsdk/src/XMPMeta-Serialize.cpp",
        "exiv2-0.25/xmpsdk/src/XMPIterator.cpp",
        "exiv2-0.25/xmpsdk/src/XMPUtils.cpp",
        "exiv2-0.25/xmpsdk/src/XMPUtils-FileInfo.cpp",
        "exiv2-0.25/xmpsdk/src/XMPCore_Impl.cpp",
        "exiv2-0.25/xmpsdk/src/ExpatAdapter.cpp",
        "exiv2-0.25/xmpsdk/src/ParseRDF.cpp",
        "exiv2-0.25/xmpsdk/src/UnicodeConversions.cpp",
        "exiv2-0.25/xmpsdk/src/MD5.cpp",
        "exiv2-0.25/xmpsdk/src/WXMPMeta.cpp",
        "exiv2-0.25/xmpsdk/src/WXMPIterator.cpp",
        "exiv2-0.25/xmpsdk/src/WXMPUtils.cpp"
      ],
      "cflags": [ 
        "-Wdeprecated-declarations"
      ],
      "cflags_cc": [
        "-fexceptions",
        "-funsigned-char",
        "-DEXV_HAVE_STDINT_H=1"
      ],
      "conditions": [ 
        [ "OS!='win'", {
          "libraries+":["-L./build/Release/libexpat.a"],
          "cflags_cc+": ["-DEXV_HAVE_STDINT_H=1"]
        } ],
        [ "OS=='win'", {"cflags_cc+": ["-DEXV_HAVE_STDINT_H=0"]} ]
      ],
      "dependencies": [
        "libexpat/libexpat.gyp:expat"
      ]
    },
    {
      'target_name': 'libexiv2',
      "type": "static_library",
      "include_dirs": [
        'exiv2-0.25/xmpsdk/include/',
        'exiv2-0.25/include/exiv2',
        'exiv2-0.25/config' 
      ],
      "sources": [
        "exiv2-0.25/src/basicio.cpp",
        "exiv2-0.25/src/bmpimage.cpp",
        "exiv2-0.25/src/canonmn.cpp",
        "exiv2-0.25/src/casiomn.cpp",
        "exiv2-0.25/src/convert.cpp",
        "exiv2-0.25/src/cr2image.cpp",
        "exiv2-0.25/src/crwimage.cpp",
        "exiv2-0.25/src/datasets.cpp",
        "exiv2-0.25/src/easyaccess.cpp",
        "exiv2-0.25/src/epsimage.cpp",
        "exiv2-0.25/src/error.cpp",
        "exiv2-0.25/src/exif.cpp",
        "exiv2-0.25/src/futils.cpp",
        "exiv2-0.25/src/fujimn.cpp",
        "exiv2-0.25/src/gifimage.cpp",
        "exiv2-0.25/src/http.cpp",
        "exiv2-0.25/src/image.cpp",
        "exiv2-0.25/src/iptc.cpp",
        "exiv2-0.25/src/jp2image.cpp",
        "exiv2-0.25/src/jpgimage.cpp",
        "exiv2-0.25/src/makernote.cpp",
        "exiv2-0.25/src/metadatum.cpp",
        "exiv2-0.25/src/minoltamn.cpp",
        "exiv2-0.25/src/mrwimage.cpp",
        "exiv2-0.25/src/nikonmn.cpp",
        "exiv2-0.25/src/olympusmn.cpp",
        "exiv2-0.25/src/orfimage.cpp",
        "exiv2-0.25/src/panasonicmn.cpp",
        "exiv2-0.25/src/pentaxmn.cpp",
        "exiv2-0.25/src/pgfimage.cpp",
        "exiv2-0.25/src/pngimage.cpp",
        "exiv2-0.25/src/pngchunk.cpp",
        "exiv2-0.25/src/preview.cpp",
        "exiv2-0.25/src/properties.cpp",
        "exiv2-0.25/src/psdimage.cpp",
        "exiv2-0.25/src/rafimage.cpp",
        "exiv2-0.25/src/rw2image.cpp",
        "exiv2-0.25/src/samsungmn.cpp",
        "exiv2-0.25/src/ssh.cpp",
        "exiv2-0.25/src/sigmamn.cpp",
        "exiv2-0.25/src/sonymn.cpp",
        "exiv2-0.25/src/tags.cpp",
        "exiv2-0.25/src/tgaimage.cpp",
        "exiv2-0.25/src/tiffcomposite.cpp",
        "exiv2-0.25/src/tiffimage.cpp",
        "exiv2-0.25/src/tiffvisitor.cpp",
        "exiv2-0.25/src/types.cpp",
        "exiv2-0.25/src/value.cpp",
        "exiv2-0.25/src/version.cpp",
        "exiv2-0.25/src/xmp.cpp",
        "exiv2-0.25/src/xmpsidecar.cpp",
        "exiv2-0.25/src/asfvideo.cpp",
        "exiv2-0.25/src/matroskavideo.cpp",
        "exiv2-0.25/src/quicktimevideo.cpp",
        "exiv2-0.25/src/riffvideo.cpp",
        "exiv2-0.25/src/utilsvideo.cpp"
      ],
      "cflags_cc": [
        "-fexceptions",
        "-frtti"
      ],
      "conditions": [ 
        [ "OS=='win'", {
          "libraries+":[
            "-L./build/Release/XMPSDK.a",
            "-L./build/Release/libexpat.a"
          ],
          "cflags_cc+": ["-DEXV_HAVE_STDINT_H=0", "-DEXV_MSC_VER=2000"]
        } ],
        [ "OS=='linux'", {
          "libraries+":["-Wl,-rpath,./build/Release/XMPSDK.a"],
          "cflags_cc+": [
            "-DEXV_HAVE_STDINT_H=1",
            "-DEXV_LOCALEDIR=\"/usr/local/share/locale\""
          ]
        }]
      ],
      #"conditions": [ [ "OS=='linux'", {"cflags_cc+": [
      #  "-DEXV_HAVE_STDINT_H=1",
      #  "-DEXV_LOCALEDIR=\"/usr/local/share/locale\""
      #]} ] ],
      #"conditions": [ [ "OS=='linux'", {"libraries+":["-Wl,-rpath,./build/Release/XMPSDK.a"]} ] ],
      #"conditions": [ [ "OS=='win'", {"libraries+":[
      #  "-L./build/Release/XMPSDK.a",
      #  "-L./build/Release/libexpat.a"
      #]} ] ],
      "dependencies": [
        "XMPSDK"
      ]
    }
  ]
}
