# FB Mangler

Facebook loooooves tracking you, and even
[embeds their tracking codes](https://twitter.com/oasace/status/1149181539000864769)
inside of images uploaded there. Thankfully, removing them is a relatively
simple matter, made even simpler with this tiny lil' script.

## Usage

The easiest way is downloading this repo as *.zip, extracting it wherever
and running `py fbmangler.py`. Do note, that there are a few requirements:

* [jamesacampbell/iptcinfo3](https://github.com/jamesacampbell/iptcinfo3)
is needed to parse and edit file metadata
* Python 3 is required to run it

Or you can use the dist files and stuff if you want to use it as a library
in your own piece of software. It's MIT, so go wild.

## Notes

If you parse parsed files again, it will still show that tracking tokens
got changed. That's because they're detected by the `FBMD` prefix, and the
replacement codes also start with that. You can pretty easily tell that
tokens aren;t original, because Facebook's tokens have a lot of 0s in them.

Why not just remove that data instead of mangling it? Well, removed data
will do nothing to them, mangled data might just screw up an algorithm of
theirs or two.