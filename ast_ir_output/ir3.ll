; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.8372795069725211921" = internal constant [3 x i8] c"%d\00"
@".str.170774002489608625" = internal constant [3 x i8] c"%f\00"
@".str.3693790085204977514" = internal constant [3 x i8] c"%s\00"
@".str.332649807079450794" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  %"b" = alloca i32
  store i32 0, i32* %"b"
  %".4" = load i32, i32* %"a"
  %".5" = icmp ne i32 %".4", 0
  br i1 %".5", label %"and.right", label %"and.end"
and.right:
  %".7" = load i32, i32* %"b"
  %".8" = icmp ne i32 %".7", 0
  br label %"and.end"
and.end:
  %".10" = phi  i1 [0, %"entry"], [%".8", %"and.right"]
  %".11" = zext i1 %".10" to i32
  %"c" = alloca i32
  store i32 %".11", i32* %"c"
  %".13" = load i32, i32* %"a"
  %".14" = icmp ne i32 %".13", 0
  br i1 %".14", label %"or.end", label %"or.right"
or.right:
  %".16" = load i32, i32* %"b"
  %".17" = icmp ne i32 %".16", 0
  br label %"or.end"
or.end:
  %".19" = phi  i1 [1, %"and.end"], [%".17", %"or.right"]
  %".20" = zext i1 %".19" to i32
  %"d" = alloca i32
  store i32 %".20", i32* %"d"
  %".22" = load i32, i32* %"a"
  %".23" = load i32, i32* %"b"
  %".24" = icmp ne i32 %".22", 0
  %".25" = icmp ne i32 %".23", 0
  %".26" = xor i1 %".24", %".25"
  %".27" = zext i1 %".26" to i32
  %"e" = alloca i32
  store i32 %".27", i32* %"e"
  %".29" = load i32, i32* %"c"
  %".30" = bitcast [2 x i8]* @".str.332649807079450794" to i8*
  %".31" = bitcast [3 x i8]* @".str.8372795069725211921" to i8*
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", i32 %".29")
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".30")
  %".34" = load i32, i32* %"d"
  %".35" = bitcast [2 x i8]* @".str.332649807079450794" to i8*
  %".36" = bitcast [3 x i8]* @".str.8372795069725211921" to i8*
  %".37" = call i32 (i8*, ...) @"printf"(i8* %".36", i32 %".34")
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".35")
  %".39" = load i32, i32* %"e"
  %".40" = bitcast [2 x i8]* @".str.332649807079450794" to i8*
  %".41" = bitcast [3 x i8]* @".str.8372795069725211921" to i8*
  %".42" = call i32 (i8*, ...) @"printf"(i8* %".41", i32 %".39")
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".40")
  ret void
}
