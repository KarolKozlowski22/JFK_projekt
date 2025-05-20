; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.5790171083117608925" = internal constant [3 x i8] c"%d\00"
@".str.3106326101400431079" = internal constant [3 x i8] c"%f\00"
@".str.8444532226840933137" = internal constant [3 x i8] c"%s\00"
@".str.3514099826871306073" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %".2" = getelementptr {i32, float}, {i32, float}* @"p", i32 0, i32 0
  store i32 30, i32* %".2"
  %".4" = getelementptr {i32, float}, {i32, float}* @"p", i32 0, i32 1
  store float 0x3ffdc28f60000000, float* %".4"
  %".6" = getelementptr {i32, float}, {i32, float}* @"p", i32 0, i32 0
  %".7" = load i32, i32* %".6"
  %".8" = bitcast [3 x i8]* @".str.5790171083117608925" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".7")
  %".10" = bitcast [2 x i8]* @".str.3514099826871306073" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10")
  %".12" = getelementptr {i32, float}, {i32, float}* @"p", i32 0, i32 1
  %".13" = load float, float* %".12"
  %".14" = bitcast [3 x i8]* @".str.3106326101400431079" to i8*
  %".15" = fpext float %".13" to double
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".14", double %".15")
  %".17" = bitcast [2 x i8]* @".str.3514099826871306073" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17")
  ret void
}

@"p" = common global {i32, float} zeroinitializer