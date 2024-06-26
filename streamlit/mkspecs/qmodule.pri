QMAKE_CFLAGS_WARN_ON += -Wno-expansion-to-defined
QMAKE_CXXFLAGS_WARN_ON += -Wno-expansion-to-defined
EXTRA_DEFINES += " _X_INLINE=inline -D XK_dead_currency=0xfe6f -D _FORTIFY_SOURCE=2 -D FC_WEIGHT_EXTRABLACK=215 -D FC_WEIGHT_ULTRABLACK=FC_WEIGHT_EXTRABLACK -D GLX_GLXEXT_PROTOTYPES" _X_INLINE=inline XK_dead_currency=0xfe6f _FORTIFY_SOURCE=2 XK_ISO_Level5_Lock=0xfe13 FC_WEIGHT_EXTRABLACK=215 FC_WEIGHT_ULTRABLACK=FC_WEIGHT_EXTRABLACK GLX_GLXEXT_PROTOTYPES
EXTRA_INCLUDEPATH += /root/miniconda3/envs/streamlit/include
EXTRA_LIBDIR += /root/miniconda3/envs/streamlit/lib /croot/qt-main_1693210824277/_build_env/x86_64-conda-linux-gnu/sysroot/usr/lib64 /croot/qt-main_1693210824277/_build_env/x86_64-conda-linux-gnu/sysroot/usr/lib
!host_build|!cross_compile {
    QMAKE_LFLAGS+=-Wl,-rpath,/root/miniconda3/envs/streamlit/lib -Wl,-rpath-link,/root/miniconda3/envs/streamlit/lib -L/root/miniconda3/envs/streamlit/lib
}
QT_CPU_FEATURES.x86_64 = mmx sse sse2
QT.global_private.enabled_features = sse2 alloca_h alloca dbus dbus-linked dlopen gui network posix_fallocate reduce_exports reduce_relocations relocatable sql system-zlib testlib widgets xml zstd
QT.global_private.disabled_features = alloca_malloc_h android-style-assets avx2 private_tests gc_binaries intelcet libudev release_tools stack-protector-strong
PKG_CONFIG_EXECUTABLE = /croot/qt-main_1693210824277/_build_env/bin/pkg-config
QMAKE_LIBS_DBUS = -L/root/miniconda3/envs/streamlit/lib -ldbus-1
QMAKE_INCDIR_DBUS = /root/miniconda3/envs/streamlit/include/dbus-1.0 /root/miniconda3/envs/streamlit/lib/dbus-1.0/include
QMAKE_LIBS_LIBDL = -ldl
QT_COORD_TYPE = double
QMAKE_LIBS_ZLIB = -lz
QMAKE_LIBS_ZSTD = -L/root/miniconda3/envs/streamlit/lib -lzstd
QMAKE_INCDIR_ZSTD = /root/miniconda3/envs/streamlit/include
CONFIG += sse2 aesni compile_examples enable_new_dtags largefile optimize_size precompile_header rdrnd rdseed shani sse3 ssse3 sse4_1 sse4_2 x86SimdAlways
QT_BUILD_PARTS += libs tools
QT_HOST_CFLAGS_DBUS += -I/root/miniconda3/envs/streamlit/include/dbus-1.0 -I/root/miniconda3/envs/streamlit/lib/dbus-1.0/include
