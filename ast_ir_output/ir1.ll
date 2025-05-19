; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.6658440445434400440" = internal constant [3 x i8] c"%d\00"
@".str.9011845808571790903" = internal constant [3 x i8] c"%f\00"
@".str.3758218351999552703" = internal constant [3 x i8] c"%s\00"
@".str.3347073341543062685" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %"b" = alloca i32
  store i32 0, i32* %"b"
  %".4" = load i32, i32* %"a"
  %".5" = icmp ne i32 %".4", 0
  br i1 %".5", label %"if.then", label %"if.else"
if.then:
  store i32 1, i32* %"b"
  br label %"if.end"
if.else:
  store i32 2, i32* %"b"
  br label %"if.end"
if.end:
  %".11" = load i32, i32* %"b"
  %".12" = bitcast [2 x i8]* @".str.3347073341543062685" to i8*
  %".13" = bitcast [3 x i8]* @".str.6658440445434400440" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %".11")
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".12")
  ret void
}
