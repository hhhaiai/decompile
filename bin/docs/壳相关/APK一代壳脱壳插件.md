# 脱壳

> https://mp.weixin.qq.com/s/o2CQeG26_qZcU1B_IrFCJw

## 介绍

现在安卓应用加壳技术越来越成熟，安全保护效果越来越好。

本文介绍的插件并不能解决方法代码抽取保护壳和VMP保护壳，以及native转换的方法。

不要指望一个简单方法解决所有问题哦。不然加壳公司就没法干了。

但是目前市场上仍然有很多安卓一代加壳技术保护的应用，针对这些应用，本文介绍的插件，可以说是最简单的脱壳方式了。

本技术参考文章：`https://bbs.pediy.com/thread-224105.htm`

但是这篇文章没有给出代码实现，本文根据作者思路，实现代码，并进行一些优化，实现如下。

完整实现参考：`https://github.com/fooree/fooXposed/tree/master/DumpDex`

## 代码

``` java
public class DexHook implements IXposedHookZygoteInit, IXposedHookLoadPackage {

    private static final String TAG = DexHook.class.getSimpleName();
    private static final File DUMP_PATH = new File("/data/local/tmp/dumpdex/");
    private final XSharedPreferences shares = new XSharedPreferences(Constants.THIS_MODULE, Constants.HOOK_CONFIG);

    @Override
    public void handleLoadPackage(final LoadPackageParam lp) throws Throwable {
        if (Build.VERSION.SDK_INT < 19 || Build.VERSION.SDK_INT > 25) {
            return;
        }

        shares.reload();
        String pkg = shares.getString(Constants.SELECT_APPLICATION, null);
        if (lp.packageName.equals(pkg)) {
            Log.i(TAG, "Loading " + lp.packageName);

            final ClassLoader systemLoader = ClassLoader.getSystemClassLoader();
            final ClassLoader bootLoader = DexClassLoader.class.getClassLoader();

            findAndHookMethod(ClassLoader.class, "loadClass", String.class, new XC_MethodHook() {
                @Override
                protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                    ClassLoader loader = (ClassLoader) param.thisObject;
                    if (param.hasThrowable()
                            || loader == bootLoader
                            || loader == systemLoader
                            || loader.getParent() == systemLoader) {
                        return;
                    }

                    Class<?> clazz = (Class<?>) param.getResult();
                    Object dex = XposedHelpers.callMethod(clazz, "getDex");
                    byte[] data = (byte[]) XposedHelpers.callMethod(dex, "getBytes");

                    File file = new File(DUMP_PATH, data.length + ".dex");
                    if (!file.exists() && file.createNewFile()) {
                        file.setReadable(true, false);
                        IO.write(data, file);
                    }
                }
            });
        }
    }

    @Override
    public void initZygote(StartupParam startupParam) throws Throwable {
        if (DUMP_PATH.exists()) return;
        DUMP_PATH.mkdirs();
        DUMP_PATH.setReadable(true, false);
        DUMP_PATH.setWritable(true, false);
    }

    static class IO implements Runnable {

        private final byte[] data;
        private final File file;

        private IO(byte[] data, File file) {
            this.data = data;
            this.file = file;
        }

        @Override
        public void run() {
            Log.i(TAG, "dump dex => " + file);
            try (BufferedOutputStream output = new BufferedOutputStream(new FileOutputStream(file))) {
                output.write(data);
            } catch (Exception e) {
                Log.e(TAG, "Dump Dex Exception", e);
            }
        }

        static void write(final byte[] data, final File file) {
            new Thread(new IO(data, file)).start();
        }
    }
}
```

