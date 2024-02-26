// Load a DEF file with Dialog
// Saved the last browsed path in the Database

// This file is donated by Dietrich Teickner.

#include <idc.idc>

#define	VERBOSE	1
#define WITHSELFEDITED 1

static main(void)
{
	auto	defFileName, defFile, w, p, modulImport;

	defFileName = AskFileEx(0,"*.def","Choose a definition-file");
	modulImport = defFileName;
	while (1) {
		p = strstr(modulImport,"\\");
		if (-1 == p) break;
		modulImport = substr(modulImport,p+1,-1);
	};
	p = strstr(modulImport,".");
	if (-1 < p)
		modulImport = substr(modulImport,0,p);
	modulImport = translate(modulImport);

	if(VERBOSE)	msg("Opening definition file %s\n", defFileName);

	defFile = fopen(defFileName, "rb");

	if (0 != defFile)
	{
		auto defline, ea, bea, sea, eea, newName, oldName, badName, x, z, id;

		//
		// Process all of the DEF's in this file.
		//
		if(VERBOSE)	msg("Processing %s\n", defFileName);

		defline = "";

		do
		{
			defline = ReadDefLine(defFile);
			if (strlen(defline) == 0) break;
			w = wordn(defline,1);
			w = translate(w);
			if ("LIBRARY" == w) {
				w = wordn(substr(defline,strlen(w)+1,-1),1);
				if (strlen(w) > 0) modulImport = w;
				continue;
			}
			if ("EXPORTS" != w) continue;
			if (strlen(modulImport) == 0) break;
			sea = get_first_seg();
			while ((-1 != sea) & (get_segm_name(sea) != modulImport)) {
				sea = get_next_seg(sea);
			}
			if (-1 == sea) break;
			w = get_segm_name(sea);
			eea = get_segm_end(sea);
			do
			{
				defline = ReadDefLine(defFile);
				if (strlen(defline) == 0) break;
				p = strstr(defline," @");
				if (0 > p) continue;
				w = substr(defline,p+2,-1);
				defline = substr(defline,0,p);
				w = wordn(w,1); /* import-number */
				w = translate(modulImport)+"_"+w;
				newName = w+"_"+wordn(defline,1);
				if (WITHSELFEDITED) {
					z = wordn(defline,1);
					badName = z+"_"+w;
					p = strstr(z,"@");
					if (p != -1) {
						x = substr(z,0,p);
						badName = badName+" "+x+" "+w+"_"+x+" "+x+"_"+w;
					}
					while (substr(z,0,1) == "_") {
						z = substr(z,1,-1);
						badName = badName+" "+z+" "+w+"_"+z+" "+z+"_"+w;
						if (p != -1) {
							x = substr(x,1,-1);
							badName = badName+" "+x+" "+w+"_"+x+" "+x+"_"+w;
						}
					}
					z = " "+newName+" "+w+" "+defline+" "+badName+" ";
				} else {
					z = " "+newName+" "+w+" "+defline+" ";
				}
				x = "__imp_";
				p = strlen(x);
				for (ea = sea;ea < eea;ea++) {
					oldName = Name(ea);
					if (strstr(z," "+oldName+" ") != -1) break;
					if (strstr(oldName,x) != 0) continue;
					if (strstr(z," "+substr(oldName,p,-1)+" ") != -1) break;
				}
				if (ea == eea) continue;
				p = strstr(defline,"@");
				if (-1 != p) {
					z = substr(defline,p+1,-1);
					z = wordn(z,1);
					z = atol(z);
					p = get_frame_args_size(ea);
					if (p != z) {
						set_frame_size(ea,get_frame_lvar_size(ea),get_frame_regs_size(ea),z);
						auto_wait();
					}
				}
				if (oldName != newName)	{
					set_name(ea ,newName);
					if(VERBOSE)	msg("--> %x,%s->%s\n", ea, oldName, newName);
				}
			}
			while (strlen(defline) > 0);
		}
		while (strlen(defline) > 0);
    	fclose(defFile);
	}
}

static wordn(c,i) {
	auto t, l, p, s;
	p = 0;
	l = strlen(c);
	t = "";
	while (0 < i) {
		i = i-1;
		while ((p < l) & (" " == substr(c,p,p+1))) p++;
		while (p < l) {
			s = substr(c,p,++p);
			if (s == " ") break;
			if (i == 0) t = t + s;
		}
	}
	return (t);
}

static translate(c) {
	auto s,t;
	s = "abcdefghijklmnopqrst";
	t = "ABCDEFGHIJKLMNOPQRST";
	return translate2(c,s,t);
}

static translate2(c,s,t) {
	auto i,j,k,l;
	l = strlen(s) - strlen(t);
	for (i = 0;i < l;i++) {
		t = t + " ";
	}
	l = strlen(c);
	for (i = 0;i < l;i++) {
		k = substr(c,i,i+1);
		j = strstr(s,k);
		if (0 <= j) {
			c = substr(c,0,i) + substr(t,j,j+1) + substr(c,i+1,-1);
		}
	}
	return c;
}

static ReadDefLine(defFile)
{
	auto line, wordstr, c, delim, i, first;

	delim = ""+0x0d+" "+0x09+0x0a;

	do {

		line = "";
		i = 0;
		first = 1;

		do {
			wordstr = "";
			c = "";
			do {
				wordstr = wordstr + c;
				c = fgetc(defFile);
				if (-1 != c) {
					i = strstr(delim,c);
				} else i = - 2;
			} while (-1 == i);
			if (strlen(wordstr) > 0) {
				if (!first) line = line + " ";
				first = 0;
				line = line + wordstr;
			};
		} while (0 < i);
		if ((strlen(line) > 0) & (substr(line,0,1) == ";")) line = "";
	} while ((strlen(line) == 0) & (0 == i));
	return(line);
}

static getPath(fileName) {
	auto	pos, path;
	path = "";
	while (1) {
		pos = strstr(fileName,"\\");
		if (-1 == pos) break;
		path = path + substr(fileName,0,pos+1);
		fileName = substr(fileName,pos+1,-1);
	}
	return path;
}

static AskFileEx(forSave, ext, dialogText) {
	auto	fileName, w, p, extArrayId, lastPath, newPath, extKey;
	w = ext;
	if (substr(w,0,1) == "*") w = substr(w,1,-1);
	if (substr(w,0,1) == ".") w = substr(w,1,-1);
/* is case-sensitive */
	extKey = "DT#"+w;
	extArrayId = get_array_id("DT#EXT#Array");
	if (-1 == extArrayId)
		extArrayId = create_array("DT#EXT#Array");
	lastPath = get_hash_string(extArrayId,extKey);
/* without this, we have at first only '*' as Mask, but not "*.ext". IDA 4.20 */
	if ("" == lastPath)
		lastPath = getPath(get_root_filename());
	w = lastPath+"*."+w;
	if(VERBOSE)	msg("--> lastPath %s\n", w);
	fileName = askfile(forSave,w,dialogText);
	if (("" == fileName) | (-1 == extArrayId))
		return fileName;
	newPath = getPath(fileName);
	if (("" != newPath) & (lastPath != newPath))
// Save the new path, associated with the extension in the Database
		set_hash_string(extArrayId, extKey, newPath);
	return fileName;
}

